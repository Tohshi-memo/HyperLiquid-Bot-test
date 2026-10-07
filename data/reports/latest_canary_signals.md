# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T18:37:31.670576+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `13`; crypto_alt avg `0.0129` n `235`; crypto_major avg `0.1627` n `8`; equity avg `-0.0129` n `150`; fx avg `-0.0008` n `6`; index avg `0.0044` n `26`; metal avg `-0.0171` n `20`; unknown avg `0.0499` n `1077`
- 1h: commodity avg `0.1669` n `13`; crypto_alt avg `0.2082` n `235`; crypto_major avg `0.0323` n `8`; equity avg `0.0002` n `150`; fx avg `0.008` n `6`; index avg `0.0104` n `26`; metal avg `-0.05` n `20`; unknown avg `-0.1808` n `1075`
- 4h: commodity avg `-0.3274` n `13`; crypto_alt avg `0.6402` n `235`; crypto_major avg `-0.047` n `8`; equity avg `0.267` n `150`; fx avg `-0.0089` n `6`; index avg `0.1144` n `26`; metal avg `0.0346` n `20`; unknown avg `0.3197` n `1068`
- 24h: commodity avg `0.4338` n `13`; crypto_alt avg `-4.7752` n `235`; crypto_major avg `-3.6261` n `8`; equity avg `-1.5083` n `150`; fx avg `-0.172` n `6`; index avg `-0.2362` n `26`; metal avg `-0.668` n `20`; unknown avg `15.3108` n `988`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
