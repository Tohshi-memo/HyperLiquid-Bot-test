# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T23:54:26.832302+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0067` n `12`; crypto_alt avg `0.0528` n `228`; crypto_major avg `0.0728` n `8`; equity avg `0.0453` n `88`; fx avg `0.0117` n `6`; index avg `-0.0094` n `23`; metal avg `-0.0404` n `20`; unknown avg `-0.1373` n `765`
- 1h: commodity avg `0.0382` n `12`; crypto_alt avg `0.0478` n `228`; crypto_major avg `0.1938` n `8`; equity avg `0.1479` n `88`; fx avg `0.0156` n `6`; index avg `-0.0086` n `23`; metal avg `-0.0894` n `20`; unknown avg `-0.4165` n `765`
- 4h: commodity avg `-0.0069` n `12`; crypto_alt avg `-0.372` n `228`; crypto_major avg `-0.2982` n `8`; equity avg `0.2557` n `88`; fx avg `0.006` n `6`; index avg `-0.0274` n `23`; metal avg `-0.2387` n `20`; unknown avg `-0.3042` n `765`
- 24h: commodity avg `0.1822` n `12`; crypto_alt avg `-2.1135` n `228`; crypto_major avg `-2.0335` n `8`; equity avg `1.3212` n `88`; fx avg `0.1286` n `6`; index avg `0.2424` n `23`; metal avg `-0.1783` n `20`; unknown avg `7.65` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
