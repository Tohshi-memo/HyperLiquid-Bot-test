# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T11:07:35.782998+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.1328` n `230`; crypto_major avg `-0.0665` n `8`; equity avg `0.2048` n `107`; fx avg `-0.0117` n `6`; index avg `0.0142` n `25`; metal avg `-0.0485` n `20`; unknown avg `-0.0128` n `781`
- 1h: commodity avg `-0.2653` n `12`; crypto_alt avg `0.0312` n `230`; crypto_major avg `0.3523` n `8`; equity avg `0.7165` n `107`; fx avg `-0.0208` n `6`; index avg `0.0617` n `25`; metal avg `0.073` n `20`; unknown avg `0.062` n `781`
- 4h: commodity avg `-0.0493` n `12`; crypto_alt avg `0.1212` n `230`; crypto_major avg `0.3289` n `8`; equity avg `0.6651` n `107`; fx avg `0.0206` n `6`; index avg `0.0411` n `25`; metal avg `0.0406` n `20`; unknown avg `0.9296` n `781`
- 24h: commodity avg `0.1838` n `12`; crypto_alt avg `1.0658` n `230`; crypto_major avg `1.5058` n `8`; equity avg `4.7687` n `107`; fx avg `0.0983` n `6`; index avg `0.4831` n `25`; metal avg `0.3025` n `20`; unknown avg `0.8676` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
