# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T07:07:28.007222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1156` n `13`; crypto_alt avg `0.0315` n `234`; crypto_major avg `-0.0552` n `8`; equity avg `-0.0869` n `142`; fx avg `0.0198` n `6`; index avg `-0.0106` n `26`; metal avg `-0.0095` n `20`; unknown avg `0.2015` n `973`
- 1h: commodity avg `0.2794` n `13`; crypto_alt avg `0.1133` n `234`; crypto_major avg `-0.0692` n `8`; equity avg `-0.2428` n `142`; fx avg `0.0154` n `6`; index avg `-0.0651` n `26`; metal avg `-0.1538` n `20`; unknown avg `0.4688` n `972`
- 4h: commodity avg `0.004` n `13`; crypto_alt avg `0.7606` n `234`; crypto_major avg `0.7005` n `8`; equity avg `0.5833` n `142`; fx avg `0.0044` n `6`; index avg `0.0871` n `26`; metal avg `0.053` n `20`; unknown avg `0.6278` n `940`
- 24h: commodity avg `0.0686` n `13`; crypto_alt avg `2.2209` n `234`; crypto_major avg `1.9377` n `8`; equity avg `0.9292` n `142`; fx avg `0.1571` n `6`; index avg `0.2229` n `26`; metal avg `-0.1697` n `20`; unknown avg `776.1538` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
