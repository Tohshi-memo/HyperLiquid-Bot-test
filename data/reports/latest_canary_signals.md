# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T21:37:20.764889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.6` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.2427` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-1.185` n `12`; crypto_alt avg `0.4205` n `228`; crypto_major avg `0.3343` n `8`; equity avg `-0.0785` n `69`; fx avg `-0.0106` n `6`; index avg `-0.0035` n `23`; metal avg `0.0031` n `18`; unknown avg `0.8238` n `422`
- 1h: commodity avg `0.5877` n `12`; crypto_alt avg `1.1063` n `228`; crypto_major avg `0.6453` n `8`; equity avg `0.143` n `69`; fx avg `-0.0295` n `6`; index avg `0.0241` n `23`; metal avg `-0.0272` n `18`; unknown avg `1.7024` n `422`
- 4h: commodity avg `0.4767` n `12`; crypto_alt avg `-0.4737` n `228`; crypto_major avg `-0.9311` n `8`; equity avg `0.4255` n `69`; fx avg `-0.0243` n `6`; index avg `0.3116` n `23`; metal avg `0.0827` n `18`; unknown avg `0.0532` n `422`
- 24h: commodity avg `0.5677` n `12`; crypto_alt avg `-2.669` n `228`; crypto_major avg `-4.139` n `8`; equity avg `1.1691` n `69`; fx avg `0.0526` n `6`; index avg `0.7521` n `23`; metal avg `0.4606` n `18`; unknown avg `-0.078` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
