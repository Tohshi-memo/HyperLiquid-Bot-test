# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T04:52:27.920650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0198` n `13`; crypto_alt avg `-0.13` n `237`; crypto_major avg `-0.0898` n `8`; equity avg `0.0211` n `151`; fx avg `-0.0003` n `6`; index avg `-0.0063` n `26`; metal avg `-0.013` n `20`; unknown avg `1.4554` n `1200`
- 1h: commodity avg `-0.0449` n `13`; crypto_alt avg `-0.2686` n `237`; crypto_major avg `-0.1796` n `8`; equity avg `-0.1215` n `151`; fx avg `-0.0169` n `6`; index avg `-0.0366` n `26`; metal avg `-0.0571` n `20`; unknown avg `1.4594` n `1192`
- 4h: commodity avg `0.0852` n `13`; crypto_alt avg `-0.3158` n `237`; crypto_major avg `-0.5825` n `8`; equity avg `-0.4162` n `151`; fx avg `-0.0266` n `6`; index avg `-0.0563` n `26`; metal avg `-0.1781` n `20`; unknown avg `1.6214` n `1191`
- 24h: commodity avg `-0.0025` n `13`; crypto_alt avg `2.2017` n `237`; crypto_major avg `1.2901` n `8`; equity avg `2.3624` n `151`; fx avg `-0.0084` n `6`; index avg `0.33` n `26`; metal avg `-0.206` n `20`; unknown avg `220.9512` n `990`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
