# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T21:52:28.762424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0368` n `12`; crypto_alt avg `-0.2139` n `234`; crypto_major avg `-0.1396` n `8`; equity avg `0.0425` n `142`; fx avg `-0.0065` n `6`; index avg `0.0063` n `26`; metal avg `-0.0054` n `20`; unknown avg `0.0048` n `975`
- 1h: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.2191` n `234`; crypto_major avg `-0.0053` n `8`; equity avg `-0.1067` n `142`; fx avg `0.0136` n `6`; index avg `-0.0193` n `26`; metal avg `-0.0109` n `20`; unknown avg `4.1492` n `971`
- 4h: commodity avg `-0.1155` n `12`; crypto_alt avg `-0.9561` n `234`; crypto_major avg `-0.1485` n `8`; equity avg `-0.1987` n `142`; fx avg `0.0175` n `6`; index avg `-0.1054` n `26`; metal avg `0.0799` n `20`; unknown avg `1.3329` n `887`
- 24h: commodity avg `0.2645` n `12`; crypto_alt avg `-0.222` n `234`; crypto_major avg `0.7788` n `8`; equity avg `-0.49` n `142`; fx avg `0.0868` n `6`; index avg `-0.065` n `26`; metal avg `-0.227` n `20`; unknown avg `780.0657` n `796`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
