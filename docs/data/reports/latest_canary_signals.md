# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T08:07:27.570400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0172` n `12`; crypto_alt avg `-0.0403` n `234`; crypto_major avg `-0.1069` n `8`; equity avg `-0.0199` n `140`; fx avg `0.0281` n `6`; index avg `0.0013` n `26`; metal avg `0.0042` n `20`; unknown avg `0.0577` n `925`
- 1h: commodity avg `-0.0279` n `12`; crypto_alt avg `0.2757` n `234`; crypto_major avg `0.0418` n `8`; equity avg `-0.0173` n `140`; fx avg `0.0997` n `6`; index avg `0.0243` n `26`; metal avg `0.099` n `20`; unknown avg `0.108` n `925`
- 4h: commodity avg `-0.1651` n `12`; crypto_alt avg `0.5222` n `234`; crypto_major avg `0.7471` n `8`; equity avg `0.5029` n `140`; fx avg `0.046` n `6`; index avg `0.091` n `26`; metal avg `0.33` n `20`; unknown avg `-0.1594` n `863`
- 24h: commodity avg `-0.366` n `12`; crypto_alt avg `5.2285` n `234`; crypto_major avg `3.7197` n `8`; equity avg `2.0587` n `140`; fx avg `0.1819` n `6`; index avg `0.3474` n `26`; metal avg `0.6345` n `20`; unknown avg `2.3862` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
