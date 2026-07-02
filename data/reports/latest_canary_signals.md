# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T08:52:29.685815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.039` n `12`; crypto_alt avg `0.1312` n `228`; crypto_major avg `0.1338` n `8`; equity avg `0.1848` n `88`; fx avg `0.0078` n `6`; index avg `0.0253` n `25`; metal avg `0.0334` n `20`; unknown avg `-0.0703` n `763`
- 1h: commodity avg `-0.0812` n `12`; crypto_alt avg `0.347` n `228`; crypto_major avg `0.3532` n `8`; equity avg `0.4807` n `88`; fx avg `0.0046` n `6`; index avg `0.0713` n `25`; metal avg `0.2019` n `20`; unknown avg `1.4665` n `763`
- 4h: commodity avg `-0.0665` n `12`; crypto_alt avg `0.0172` n `228`; crypto_major avg `-0.348` n `8`; equity avg `-0.4548` n `88`; fx avg `-0.0504` n `6`; index avg `-0.1149` n `25`; metal avg `0.1111` n `20`; unknown avg `2.3601` n `741`
- 24h: commodity avg `-0.3739` n `12`; crypto_alt avg `2.528` n `228`; crypto_major avg `2.0027` n `8`; equity avg `-1.8131` n `88`; fx avg `-0.0602` n `6`; index avg `-0.4913` n `25`; metal avg `1.2216` n `20`; unknown avg `17.1345` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
