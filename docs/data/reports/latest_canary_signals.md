# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T12:37:37.441315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `13`; crypto_alt avg `0.334` n `234`; crypto_major avg `0.3853` n `8`; equity avg `0.618` n `142`; fx avg `-0.035` n `6`; index avg `0.1681` n `26`; metal avg `0.3711` n `20`; unknown avg `5.9311` n `985`
- 1h: commodity avg `0.046` n `13`; crypto_alt avg `0.5626` n `234`; crypto_major avg `0.3438` n `8`; equity avg `0.5293` n `142`; fx avg `-0.0463` n `6`; index avg `0.1607` n `26`; metal avg `0.2916` n `20`; unknown avg `3.3212` n `977`
- 4h: commodity avg `0.0151` n `13`; crypto_alt avg `0.2696` n `234`; crypto_major avg `0.2993` n `8`; equity avg `0.28` n `142`; fx avg `-0.0536` n `6`; index avg `0.163` n `26`; metal avg `0.1933` n `20`; unknown avg `0.4194` n `975`
- 24h: commodity avg `-0.5131` n `13`; crypto_alt avg `2.5691` n `234`; crypto_major avg `2.4155` n `8`; equity avg `1.5826` n `142`; fx avg `-0.3576` n `6`; index avg `0.34` n `26`; metal avg `0.1898` n `20`; unknown avg `0.3335` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1785`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
