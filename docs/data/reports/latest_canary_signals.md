# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T03:22:31.664696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `13`; crypto_alt avg `0.0598` n `234`; crypto_major avg `-0.0673` n `8`; equity avg `0.0311` n `142`; fx avg `-0.0001` n `6`; index avg `-0.0116` n `26`; metal avg `-0.0085` n `20`; unknown avg `0.1167` n `974`
- 1h: commodity avg `-0.1041` n `13`; crypto_alt avg `0.739` n `234`; crypto_major avg `0.06` n `8`; equity avg `0.2516` n `142`; fx avg `-0.0039` n `6`; index avg `0.051` n `26`; metal avg `0.0575` n `20`; unknown avg `-0.009` n `972`
- 4h: commodity avg `-0.0964` n `13`; crypto_alt avg `0.2938` n `234`; crypto_major avg `-0.3994` n `8`; equity avg `0.4676` n `142`; fx avg `0.0765` n `6`; index avg `0.13` n `26`; metal avg `0.068` n `20`; unknown avg `0.9159` n `942`
- 24h: commodity avg `-0.0237` n `13`; crypto_alt avg `1.1825` n `234`; crypto_major avg `0.704` n `8`; equity avg `0.433` n `142`; fx avg `0.2109` n `6`; index avg `0.1756` n `26`; metal avg `-0.1209` n `20`; unknown avg `777.3438` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
