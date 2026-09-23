# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T02:22:25.415442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `0.6023` n `234`; crypto_major avg `0.5156` n `8`; equity avg `0.0458` n `140`; fx avg `-0.0163` n `6`; index avg `-0.0024` n `26`; metal avg `0.0067` n `20`; unknown avg `-0.0534` n `945`
- 1h: commodity avg `-0.0977` n `12`; crypto_alt avg `-0.2565` n `234`; crypto_major avg `-0.1872` n `8`; equity avg `-0.3179` n `140`; fx avg `-0.0044` n `6`; index avg `-0.0506` n `26`; metal avg `-0.1015` n `20`; unknown avg `-0.0084` n `943`
- 4h: commodity avg `0.0392` n `12`; crypto_alt avg `0.7952` n `234`; crypto_major avg `0.6331` n `8`; equity avg `-0.3486` n `140`; fx avg `-0.0664` n `6`; index avg `-0.1086` n `26`; metal avg `-0.2481` n `20`; unknown avg `0.6338` n `937`
- 24h: commodity avg `0.0365` n `12`; crypto_alt avg `3.11` n `234`; crypto_major avg `1.7645` n `8`; equity avg `0.3038` n `140`; fx avg `-0.1877` n `6`; index avg `-0.0104` n `26`; metal avg `0.0514` n `20`; unknown avg `0.9832` n `836`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
