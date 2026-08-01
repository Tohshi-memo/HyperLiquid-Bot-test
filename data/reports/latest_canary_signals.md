# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T03:37:26.545234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0083` n `12`; crypto_alt avg `-0.0313` n `230`; crypto_major avg `-0.0635` n `8`; equity avg `-0.0067` n `102`; fx avg `-0.0236` n `6`; index avg `0.0055` n `25`; metal avg `-0.0015` n `20`; unknown avg `-0.0154` n `781`
- 1h: commodity avg `0.0233` n `12`; crypto_alt avg `-0.0457` n `230`; crypto_major avg `-0.1817` n `8`; equity avg `-0.0384` n `102`; fx avg `0.0004` n `6`; index avg `-0.0083` n `25`; metal avg `0.0012` n `20`; unknown avg `-0.0466` n `781`
- 4h: commodity avg `-0.1274` n `12`; crypto_alt avg `0.4182` n `230`; crypto_major avg `0.0661` n `8`; equity avg `0.0783` n `102`; fx avg `-0.014` n `6`; index avg `0.0348` n `25`; metal avg `-0.0218` n `20`; unknown avg `5.533` n `781`
- 24h: commodity avg `0.9366` n `12`; crypto_alt avg `0.1875` n `230`; crypto_major avg `-1.5516` n `8`; equity avg `-2.0791` n `102`; fx avg `-0.1442` n `6`; index avg `-0.1986` n `25`; metal avg `-0.1987` n `20`; unknown avg `4.9038` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
