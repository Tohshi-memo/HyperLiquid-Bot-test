# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T02:52:26.065132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0627` n `12`; crypto_alt avg `-0.1144` n `230`; crypto_major avg `-0.1043` n `8`; equity avg `0.0278` n `114`; fx avg `-0.0037` n `6`; index avg `0.0064` n `25`; metal avg `0.0033` n `20`; unknown avg `-0.0735` n `791`
- 1h: commodity avg `-0.064` n `12`; crypto_alt avg `-0.0618` n `230`; crypto_major avg `0.0801` n `8`; equity avg `0.068` n `114`; fx avg `-0.0055` n `6`; index avg `0.0053` n `25`; metal avg `0.0082` n `20`; unknown avg `-0.0123` n `791`
- 4h: commodity avg `0.0179` n `12`; crypto_alt avg `-0.5839` n `230`; crypto_major avg `-0.1272` n `8`; equity avg `0.0737` n `114`; fx avg `-0.0047` n `6`; index avg `0.0173` n `25`; metal avg `0.0142` n `20`; unknown avg `-0.0617` n `791`
- 24h: commodity avg `-0.0717` n `12`; crypto_alt avg `-0.2231` n `230`; crypto_major avg `-0.1018` n `8`; equity avg `0.2026` n `114`; fx avg `-0.0577` n `6`; index avg `0.0122` n `25`; metal avg `-0.0202` n `20`; unknown avg `0.0036` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2237`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1842`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1688`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
