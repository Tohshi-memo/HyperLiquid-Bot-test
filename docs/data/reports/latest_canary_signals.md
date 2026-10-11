# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T20:52:35.227868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0314` n `13`; crypto_alt avg `-0.0589` n `235`; crypto_major avg `0.0388` n `8`; equity avg `0.0001` n `150`; fx avg `0.002` n `6`; index avg `0.0027` n `26`; metal avg `-0.0014` n `20`; unknown avg `-0.0335` n `1134`
- 1h: commodity avg `0.0606` n `13`; crypto_alt avg `-0.0002` n `235`; crypto_major avg `0.0345` n `8`; equity avg `0.0138` n `150`; fx avg `0.0037` n `6`; index avg `-0.0016` n `26`; metal avg `0.0082` n `20`; unknown avg `-0.1142` n `1118`
- 4h: commodity avg `0.1335` n `13`; crypto_alt avg `-0.0742` n `235`; crypto_major avg `-0.4906` n `8`; equity avg `-0.0239` n `150`; fx avg `0.011` n `6`; index avg `-0.0052` n `26`; metal avg `0.0141` n `20`; unknown avg `0.0596` n `1100`
- 24h: commodity avg `0.3593` n `13`; crypto_alt avg `1.6332` n `235`; crypto_major avg `0.6109` n `8`; equity avg `0.2852` n `150`; fx avg `0.0247` n `6`; index avg `0.0323` n `26`; metal avg `0.088` n `20`; unknown avg `0.8212` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
