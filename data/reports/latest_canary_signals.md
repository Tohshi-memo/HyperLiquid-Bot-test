# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T11:52:30.445202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0612` n `12`; crypto_alt avg `-0.0978` n `234`; crypto_major avg `-0.192` n `8`; equity avg `-0.0522` n `141`; fx avg `0.0077` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0047` n `20`; unknown avg `10.828` n `962`
- 1h: commodity avg `0.0365` n `12`; crypto_alt avg `-0.0466` n `234`; crypto_major avg `-0.0285` n `8`; equity avg `0.1301` n `141`; fx avg `-0.0105` n `6`; index avg `0.0249` n `26`; metal avg `-0.0601` n `20`; unknown avg `7.9224` n `960`
- 4h: commodity avg `0.2877` n `12`; crypto_alt avg `0.4944` n `234`; crypto_major avg `0.5386` n `8`; equity avg `-0.1778` n `141`; fx avg `-0.0891` n `6`; index avg `0.0029` n `26`; metal avg `0.0518` n `20`; unknown avg `15.6282` n `942`
- 24h: commodity avg `-0.0408` n `12`; crypto_alt avg `-3.7551` n `234`; crypto_major avg `-2.7629` n `8`; equity avg `-2.5924` n `141`; fx avg `0.023` n `6`; index avg `-0.2342` n `26`; metal avg `-0.9162` n `20`; unknown avg `4.4637` n `814`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
