# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T09:22:28.857355+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1041` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9785` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0125` n `13`; crypto_alt avg `0.0846` n `239`; crypto_major avg `-0.0563` n `8`; equity avg `-0.0374` n `166`; fx avg `0.0217` n `6`; index avg `0.0024` n `27`; metal avg `-0.0097` n `20`; unknown avg `-0.0372` n `1260`
- 1h: commodity avg `0.016` n `13`; crypto_alt avg `0.5678` n `239`; crypto_major avg `0.6789` n `8`; equity avg `-0.0257` n `166`; fx avg `0.0443` n `6`; index avg `-0.0015` n `27`; metal avg `0.0416` n `20`; unknown avg `357.9085` n `1258`
- 4h: commodity avg `-0.0191` n `13`; crypto_alt avg `1.3259` n `239`; crypto_major avg `2.085` n `8`; equity avg `0.5947` n `166`; fx avg `-0.0333` n `6`; index avg `0.0594` n `27`; metal avg `0.1065` n `20`; unknown avg `488.353` n `1208`
- 24h: commodity avg `0.6764` n `13`; crypto_alt avg `-5.8255` n `239`; crypto_major avg `-6.6651` n `8`; equity avg `-4.8877` n `166`; fx avg `-0.0614` n `6`; index avg `-0.571` n `27`; metal avg `-0.4525` n `20`; unknown avg `183.0054` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
