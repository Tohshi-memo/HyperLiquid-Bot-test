# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T07:22:32.160565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `12`; crypto_alt avg `0.0922` n `234`; crypto_major avg `-0.0304` n `8`; equity avg `0.038` n `141`; fx avg `-0.0029` n `6`; index avg `0.0061` n `26`; metal avg `-0.0108` n `20`; unknown avg `-0.0653` n `963`
- 1h: commodity avg `-0.0375` n `12`; crypto_alt avg `0.7332` n `234`; crypto_major avg `0.3433` n `8`; equity avg `0.2407` n `141`; fx avg `-0.0021` n `6`; index avg `0.036` n `26`; metal avg `0.003` n `20`; unknown avg `0.092` n `959`
- 4h: commodity avg `-0.059` n `12`; crypto_alt avg `2.0799` n `234`; crypto_major avg `1.3999` n `8`; equity avg `0.6048` n `141`; fx avg `-0.0389` n `6`; index avg `0.0735` n `26`; metal avg `-0.0078` n `20`; unknown avg `13.0831` n `937`
- 24h: commodity avg `-0.0581` n `12`; crypto_alt avg `0.6962` n `234`; crypto_major avg `1.0212` n `8`; equity avg `-0.6933` n `141`; fx avg `-0.1061` n `6`; index avg `-0.0602` n `26`; metal avg `-0.1786` n `20`; unknown avg `65.8744` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
