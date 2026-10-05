# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T22:46:57.739585+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `13`; crypto_alt avg `0.1023` n `235`; crypto_major avg `0.0258` n `8`; equity avg `-0.0104` n `144`; fx avg `0.0028` n `6`; index avg `-0.001` n `26`; metal avg `-0.0114` n `20`; unknown avg `-0.1303` n `1079`
- 1h: commodity avg `0.0255` n `13`; crypto_alt avg `0.0394` n `235`; crypto_major avg `0.1337` n `8`; equity avg `0.0235` n `144`; fx avg `0.0283` n `6`; index avg `-0.0095` n `26`; metal avg `0.0206` n `20`; unknown avg `-0.3042` n `1075`
- 4h: commodity avg `0.0532` n `13`; crypto_alt avg `0.9899` n `235`; crypto_major avg `0.7186` n `8`; equity avg `0.2248` n `144`; fx avg `0.0272` n `6`; index avg `0.0082` n `26`; metal avg `-0.0088` n `20`; unknown avg `-0.2093` n `979`
- 24h: commodity avg `-0.2011` n `13`; crypto_alt avg `0.7087` n `235`; crypto_major avg `0.2106` n `8`; equity avg `0.2496` n `144`; fx avg `-0.0768` n `6`; index avg `0.1046` n `26`; metal avg `0.1146` n `20`; unknown avg `630.2525` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1962`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
