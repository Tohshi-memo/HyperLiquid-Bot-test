# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T23:37:33.823147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0198` n `12`; crypto_alt avg `-0.4864` n `234`; crypto_major avg `-0.2189` n `8`; equity avg `0.0087` n `142`; fx avg `-0.0078` n `6`; index avg `0.0067` n `26`; metal avg `0.0008` n `20`; unknown avg `4.3567` n `963`
- 1h: commodity avg `-0.057` n `12`; crypto_alt avg `-0.2878` n `234`; crypto_major avg `-0.1058` n `8`; equity avg `0.0163` n `142`; fx avg `-0.021` n `6`; index avg `-0.0046` n `26`; metal avg `0.0245` n `20`; unknown avg `3.2671` n `960`
- 4h: commodity avg `0.0232` n `12`; crypto_alt avg `-0.6617` n `234`; crypto_major avg `-0.1327` n `8`; equity avg `0.2131` n `142`; fx avg `-0.0046` n `6`; index avg `0.0424` n `26`; metal avg `0.0767` n `20`; unknown avg `1.8961` n `872`
- 24h: commodity avg `-0.8905` n `12`; crypto_alt avg `-0.0646` n `234`; crypto_major avg `-0.346` n `8`; equity avg `0.7267` n `142`; fx avg `-0.1445` n `6`; index avg `0.0912` n `26`; metal avg `0.2465` n `20`; unknown avg `3099.2315` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1877`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1843`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1742`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
