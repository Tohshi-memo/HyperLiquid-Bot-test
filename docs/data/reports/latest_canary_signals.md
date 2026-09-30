# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T03:52:28.453761+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0444` n `12`; crypto_alt avg `-0.2221` n `234`; crypto_major avg `-0.1707` n `8`; equity avg `-0.0586` n `142`; fx avg `0.0131` n `6`; index avg `-0.0081` n `26`; metal avg `-0.046` n `20`; unknown avg `2.1698` n `963`
- 1h: commodity avg `0.0384` n `12`; crypto_alt avg `-0.6395` n `234`; crypto_major avg `-0.4047` n `8`; equity avg `-0.0293` n `142`; fx avg `0.0155` n `6`; index avg `0.0102` n `26`; metal avg `-0.0916` n `20`; unknown avg `3.2217` n `961`
- 4h: commodity avg `0.1055` n `12`; crypto_alt avg `-0.008` n `234`; crypto_major avg `-0.1855` n `8`; equity avg `-0.309` n `142`; fx avg `-0.0177` n `6`; index avg `-0.0579` n `26`; metal avg `-0.1674` n `20`; unknown avg `2.1934` n `955`
- 24h: commodity avg `-0.9154` n `12`; crypto_alt avg `1.3232` n `234`; crypto_major avg `0.1091` n `8`; equity avg `0.9597` n `142`; fx avg `-0.1574` n `6`; index avg `0.1443` n `26`; metal avg `0.1626` n `20`; unknown avg `3246.597` n `834`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1774`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.173`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
