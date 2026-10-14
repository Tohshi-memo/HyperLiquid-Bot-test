# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T11:37:29.416858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `13`; crypto_alt avg `-0.0513` n `235`; crypto_major avg `-0.0312` n `8`; equity avg `-0.0202` n `151`; fx avg `-0.0046` n `6`; index avg `-0.0045` n `26`; metal avg `-0.0198` n `20`; unknown avg `0.6713` n `1136`
- 1h: commodity avg `-0.0849` n `13`; crypto_alt avg `0.149` n `235`; crypto_major avg `0.1245` n `8`; equity avg `-0.2254` n `151`; fx avg `0.0083` n `6`; index avg `-0.0169` n `26`; metal avg `-0.0194` n `20`; unknown avg `0.9363` n `1134`
- 4h: commodity avg `0.0068` n `13`; crypto_alt avg `-0.5767` n `235`; crypto_major avg `-0.1259` n `8`; equity avg `-0.3989` n `151`; fx avg `-0.002` n `6`; index avg `-0.0129` n `26`; metal avg `-0.0233` n `20`; unknown avg `1192.8582` n `1037`
- 24h: commodity avg `1.0592` n `13`; crypto_alt avg `0.3016` n `235`; crypto_major avg `0.231` n `8`; equity avg `-0.2656` n `151`; fx avg `0.0175` n `6`; index avg `0.0142` n `26`; metal avg `-0.4689` n `20`; unknown avg `1269.6052` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1513`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1298`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1091`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0764`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0731`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0724`, n `666`, weak_sample_signal
