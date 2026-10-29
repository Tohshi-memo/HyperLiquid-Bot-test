# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T19:37:28.961005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0178` n `13`; crypto_alt avg `0.1197` n `238`; crypto_major avg `0.0009` n `8`; equity avg `0.1835` n `156`; fx avg `0.0148` n `6`; index avg `0.0257` n `27`; metal avg `0.0375` n `20`; unknown avg `0.3139` n `1238`
- 1h: commodity avg `-0.0532` n `13`; crypto_alt avg `0.0782` n `238`; crypto_major avg `-0.1231` n `8`; equity avg `0.1705` n `156`; fx avg `0.0196` n `6`; index avg `0.0439` n `27`; metal avg `0.0617` n `20`; unknown avg `5.0945` n `1232`
- 4h: commodity avg `0.2787` n `13`; crypto_alt avg `-1.4213` n `238`; crypto_major avg `-0.995` n `8`; equity avg `-1.074` n `156`; fx avg `0.0479` n `6`; index avg `-0.0669` n `27`; metal avg `-0.0292` n `20`; unknown avg `4.5476` n `1228`
- 24h: commodity avg `-0.4922` n `13`; crypto_alt avg `-1.0891` n `238`; crypto_major avg `0.9387` n `8`; equity avg `-1.6323` n `155`; fx avg `0.0439` n `6`; index avg `-0.1626` n `27`; metal avg `-0.5076` n `20`; unknown avg `11.8123` n `946`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
