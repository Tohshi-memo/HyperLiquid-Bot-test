# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T03:07:28.055872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0263` n `13`; crypto_alt avg `0.2339` n `239`; crypto_major avg `0.2461` n `8`; equity avg `0.3764` n `162`; fx avg `0.0099` n `6`; index avg `0.0239` n `27`; metal avg `0.0837` n `20`; unknown avg `3.6039` n `1260`
- 1h: commodity avg `-0.0111` n `13`; crypto_alt avg `0.1424` n `239`; crypto_major avg `-0.1023` n `8`; equity avg `0.4139` n `162`; fx avg `0.0113` n `6`; index avg `0.032` n `27`; metal avg `0.1009` n `20`; unknown avg `0.5822` n `1262`
- 4h: commodity avg `-0.1157` n `13`; crypto_alt avg `0.0299` n `239`; crypto_major avg `-0.3832` n `8`; equity avg `0.7042` n `162`; fx avg `0.0466` n `6`; index avg `0.0647` n `27`; metal avg `0.2614` n `20`; unknown avg `167.9901` n `1258`
- 24h: commodity avg `-0.9136` n `13`; crypto_alt avg `-0.2898` n `239`; crypto_major avg `0.0561` n `8`; equity avg `-2.7592` n `162`; fx avg `-0.0401` n `6`; index avg `-0.25` n `27`; metal avg `-0.0174` n `20`; unknown avg `564.6855` n `999`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
