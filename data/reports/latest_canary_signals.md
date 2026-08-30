# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T08:07:23.638194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `0.1085` n `231`; crypto_major avg `0.0507` n `8`; equity avg `0.0048` n `128`; fx avg `0.0009` n `6`; index avg `-0.0001` n `26`; metal avg `0.005` n `20`; unknown avg `-0.0722` n `793`
- 1h: commodity avg `-0.0279` n `12`; crypto_alt avg `-0.1467` n `231`; crypto_major avg `-0.179` n `8`; equity avg `-0.0518` n `128`; fx avg `-0.0022` n `6`; index avg `-0.0105` n `26`; metal avg `0.006` n `20`; unknown avg `-0.0529` n `793`
- 4h: commodity avg `0.0032` n `12`; crypto_alt avg `0.1681` n `231`; crypto_major avg `-0.029` n `8`; equity avg `-0.0025` n `128`; fx avg `0.0062` n `6`; index avg `-0.0081` n `26`; metal avg `0.0135` n `20`; unknown avg `-0.0223` n `759`
- 24h: commodity avg `-0.0046` n `12`; crypto_alt avg `0.9943` n `231`; crypto_major avg `0.9963` n `8`; equity avg `0.2465` n `128`; fx avg `-0.0055` n `6`; index avg `0.0527` n `26`; metal avg `0.1041` n `20`; unknown avg `0.7294` n `714`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
