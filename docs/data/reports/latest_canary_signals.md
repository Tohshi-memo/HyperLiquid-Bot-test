# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T11:52:28.637747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0582` n `13`; crypto_alt avg `-0.0709` n `237`; crypto_major avg `-0.0428` n `8`; equity avg `-0.0385` n `151`; fx avg `0.0016` n `6`; index avg `-0.0123` n `26`; metal avg `-0.0402` n `20`; unknown avg `0.0896` n `1196`
- 1h: commodity avg `0.0391` n `13`; crypto_alt avg `0.0161` n `237`; crypto_major avg `0.0169` n `8`; equity avg `-0.2465` n `151`; fx avg `0.0037` n `6`; index avg `-0.0368` n `26`; metal avg `-0.0453` n `20`; unknown avg `-0.2175` n `1194`
- 4h: commodity avg `0.2002` n `13`; crypto_alt avg `-0.4901` n `237`; crypto_major avg `-0.243` n `8`; equity avg `-0.6651` n `151`; fx avg `-0.0049` n `6`; index avg `-0.1037` n `26`; metal avg `-0.0665` n `20`; unknown avg `1.1835` n `1178`
- 24h: commodity avg `0.3039` n `13`; crypto_alt avg `0.22` n `237`; crypto_major avg `-0.65` n `8`; equity avg `-2.4337` n `151`; fx avg `-0.0175` n `6`; index avg `-0.3195` n `26`; metal avg `-0.3387` n `20`; unknown avg `0.544` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
