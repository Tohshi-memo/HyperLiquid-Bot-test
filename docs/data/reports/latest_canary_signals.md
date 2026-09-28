# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T20:37:49.800705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0642` n `12`; crypto_alt avg `-0.0104` n `234`; crypto_major avg `-0.0224` n `8`; equity avg `0.01` n `141`; fx avg `-0.0037` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0478` n `20`; unknown avg `-0.221` n `963`
- 1h: commodity avg `0.0923` n `12`; crypto_alt avg `0.5539` n `234`; crypto_major avg `0.375` n `8`; equity avg `-0.1459` n `141`; fx avg `-0.0009` n `6`; index avg `-0.0183` n `26`; metal avg `-0.1274` n `20`; unknown avg `-0.2087` n `899`
- 4h: commodity avg `0.1664` n `12`; crypto_alt avg `-0.5463` n `234`; crypto_major avg `-0.6616` n `8`; equity avg `-0.4697` n `141`; fx avg `0.0109` n `6`; index avg `-0.0737` n `26`; metal avg `-0.2016` n `20`; unknown avg `4.1292` n `858`
- 24h: commodity avg `-0.2763` n `12`; crypto_alt avg `-3.6389` n `234`; crypto_major avg `-2.0169` n `8`; equity avg `-3.3876` n `141`; fx avg `0.0489` n `6`; index avg `-0.3246` n `26`; metal avg `-1.1481` n `20`; unknown avg `27.4272` n `776`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
