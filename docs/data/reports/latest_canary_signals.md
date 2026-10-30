# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T04:22:28.467464+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.9311` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.5749` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.3139` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.015` n `13`; crypto_alt avg `0.588` n `238`; crypto_major avg `0.3849` n `8`; equity avg `0.3192` n `156`; fx avg `0.0127` n `6`; index avg `0.0801` n `27`; metal avg `0.049` n `20`; unknown avg `1.183` n `1260`
- 1h: commodity avg `-0.0364` n `13`; crypto_alt avg `1.2259` n `238`; crypto_major avg `1.2073` n `8`; equity avg `0.6281` n `156`; fx avg `-0.0054` n `6`; index avg `0.1037` n `27`; metal avg `0.0063` n `20`; unknown avg `6.7719` n `1238`
- 4h: commodity avg `0.1037` n `13`; crypto_alt avg `2.5495` n `238`; crypto_major avg `2.6786` n `8`; equity avg `0.3647` n `156`; fx avg `-0.0312` n `6`; index avg `-0.0312` n `27`; metal avg `-0.2525` n `20`; unknown avg `7.074` n `1236`
- 24h: commodity avg `-0.0937` n `13`; crypto_alt avg `-3.8885` n `238`; crypto_major avg `0.023` n `8`; equity avg `-2.4657` n `155`; fx avg `0.122` n `6`; index avg `-0.2487` n `27`; metal avg `-0.6437` n `20`; unknown avg `28.5624` n `974`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
