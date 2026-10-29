# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T22:07:28.035244+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.5293` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.4671` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.3002` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0201` n `13`; crypto_alt avg `-0.9719` n `238`; crypto_major avg `-0.4988` n `8`; equity avg `-0.0434` n `156`; fx avg `0.0106` n `6`; index avg `-0.012` n `27`; metal avg `0.0277` n `20`; unknown avg `0.0118` n `1254`
- 1h: commodity avg `-0.0033` n `13`; crypto_alt avg `-1.3673` n `238`; crypto_major avg `-0.133` n `8`; equity avg `-0.438` n `156`; fx avg `-0.0055` n `6`; index avg `-0.018` n `27`; metal avg `0.0378` n `20`; unknown avg `2.2552` n `1252`
- 4h: commodity avg `0.009` n `13`; crypto_alt avg `-5.6315` n `238`; crypto_major avg `-3.4581` n `8`; equity avg `-2.3844` n `156`; fx avg `0.0118` n `6`; index avg `-0.1579` n `27`; metal avg `0.0712` n `20`; unknown avg `22.7728` n `1162`
- 24h: commodity avg `-0.2503` n `13`; crypto_alt avg `-6.4324` n `238`; crypto_major avg `-2.3429` n `8`; equity avg `-3.3101` n `155`; fx avg `0.0512` n `6`; index avg `-0.2549` n `27`; metal avg `-0.5946` n `20`; unknown avg `28.8904` n `976`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
