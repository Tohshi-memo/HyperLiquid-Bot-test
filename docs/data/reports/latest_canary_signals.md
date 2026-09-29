# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T00:07:28.222692+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0322` n `12`; crypto_alt avg `0.1431` n `234`; crypto_major avg `0.0433` n `8`; equity avg `0.0966` n `141`; fx avg `-0.0045` n `6`; index avg `0.024` n `26`; metal avg `-0.0036` n `20`; unknown avg `-0.0338` n `955`
- 1h: commodity avg `0.0139` n `12`; crypto_alt avg `0.5928` n `234`; crypto_major avg `0.1658` n `8`; equity avg `0.0625` n `141`; fx avg `-0.0225` n `6`; index avg `0.0136` n `26`; metal avg `0.0056` n `20`; unknown avg `-0.1539` n `955`
- 4h: commodity avg `0.0713` n `12`; crypto_alt avg `0.6539` n `234`; crypto_major avg `0.0166` n `8`; equity avg `0.1868` n `141`; fx avg `-0.02` n `6`; index avg `0.0201` n `26`; metal avg `0.0013` n `20`; unknown avg `-0.3029` n `887`
- 24h: commodity avg `0.0852` n `12`; crypto_alt avg `-3.1507` n `234`; crypto_major avg `-1.7034` n `8`; equity avg `-2.9787` n `141`; fx avg `0.0052` n `6`; index avg `-0.2924` n `26`; metal avg `-0.9165` n `20`; unknown avg `90.6289` n `804`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
