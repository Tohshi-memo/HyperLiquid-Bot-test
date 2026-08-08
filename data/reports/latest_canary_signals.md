# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T12:22:37.551861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `0.0261` n `230`; crypto_major avg `-0.0063` n `8`; equity avg `0.0196` n `112`; fx avg `0.0037` n `6`; index avg `0.0117` n `25`; metal avg `0.0051` n `20`; unknown avg `0.0335` n `784`
- 1h: commodity avg `0.0233` n `12`; crypto_alt avg `0.1537` n `230`; crypto_major avg `0.0` n `8`; equity avg `-0.0047` n `112`; fx avg `0.0005` n `6`; index avg `-0.0003` n `25`; metal avg `-0.0103` n `20`; unknown avg `-0.001` n `784`
- 4h: commodity avg `0.0604` n `12`; crypto_alt avg `0.333` n `230`; crypto_major avg `0.3081` n `8`; equity avg `0.1688` n `112`; fx avg `-0.0047` n `6`; index avg `0.0237` n `25`; metal avg `-0.0049` n `20`; unknown avg `1.2516` n `784`
- 24h: commodity avg `0.0957` n `12`; crypto_alt avg `0.1787` n `230`; crypto_major avg `-0.147` n `8`; equity avg `0.7384` n `112`; fx avg `-0.0414` n `6`; index avg `0.0211` n `25`; metal avg `0.1347` n `20`; unknown avg `1.0258` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
