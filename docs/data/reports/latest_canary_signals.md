# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T20:52:29.858095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0124` n `13`; crypto_alt avg `0.0252` n `237`; crypto_major avg `0.0168` n `8`; equity avg `-0.0329` n `151`; fx avg `0.0046` n `6`; index avg `0.0013` n `26`; metal avg `0.0028` n `20`; unknown avg `0.3965` n `1194`
- 1h: commodity avg `0.019` n `13`; crypto_alt avg `-0.075` n `237`; crypto_major avg `0.0205` n `8`; equity avg `-0.0004` n `151`; fx avg `0.0039` n `6`; index avg `0.0017` n `26`; metal avg `-0.0264` n `20`; unknown avg `11.7226` n `1178`
- 4h: commodity avg `0.0231` n `13`; crypto_alt avg `-1.7514` n `237`; crypto_major avg `-0.7241` n `8`; equity avg `-0.3165` n `151`; fx avg `-0.0094` n `6`; index avg `-0.0574` n `26`; metal avg `-0.042` n `20`; unknown avg `2.367` n `1158`
- 24h: commodity avg `0.0488` n `13`; crypto_alt avg `-5.2922` n `236`; crypto_major avg `-2.5279` n `8`; equity avg `-1.261` n `151`; fx avg `-0.0179` n `6`; index avg `-0.1598` n `26`; metal avg `-0.0988` n `20`; unknown avg `1.538` n `1007`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2101`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1444`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1395`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1205`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0779`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
