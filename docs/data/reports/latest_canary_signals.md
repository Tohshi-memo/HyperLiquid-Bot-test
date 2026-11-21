# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T07:22:24.101262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `3.4636` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `3.3132` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.4389` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0245` n `13`; crypto_alt avg `-0.2883` n `239`; crypto_major avg `-0.0811` n `8`; equity avg `-0.0436` n `166`; fx avg `0.0011` n `6`; index avg `-0.0055` n `27`; metal avg `-0.0152` n `20`; unknown avg `158.6484` n `1260`
- 1h: commodity avg `-0.0294` n `13`; crypto_alt avg `2.1727` n `239`; crypto_major avg `3.4342` n `8`; equity avg `0.9953` n `166`; fx avg `-0.0837` n `6`; index avg `0.0895` n `27`; metal avg `0.121` n `20`; unknown avg `320.7063` n `1250`
- 4h: commodity avg `-0.0825` n `13`; crypto_alt avg `-0.6538` n `239`; crypto_major avg `0.2441` n `8`; equity avg `-0.013` n `166`; fx avg `-0.1121` n `6`; index avg `0.0315` n `27`; metal avg `0.0019` n `20`; unknown avg `164.9194` n `1216`
- 24h: commodity avg `0.3491` n `13`; crypto_alt avg `-5.4387` n `239`; crypto_major avg `-6.1972` n `8`; equity avg `-4.5722` n `166`; fx avg `-0.1469` n `6`; index avg `-0.4837` n `27`; metal avg `-0.1275` n `20`; unknown avg `17.6852` n `1105`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
