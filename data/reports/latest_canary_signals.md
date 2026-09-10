# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T00:22:35.907810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0828` n `12`; crypto_alt avg `-0.3825` n `233`; crypto_major avg `-0.1718` n `8`; equity avg `-0.0764` n `134`; fx avg `-0.0154` n `6`; index avg `-0.0202` n `26`; metal avg `0.0263` n `20`; unknown avg `-0.0914` n `797`
- 1h: commodity avg `-0.1328` n `12`; crypto_alt avg `-0.1291` n `233`; crypto_major avg `0.0107` n `8`; equity avg `0.0592` n `134`; fx avg `-0.001` n `6`; index avg `0.0379` n `26`; metal avg `-0.0342` n `20`; unknown avg `0.5601` n `795`
- 4h: commodity avg `-0.0817` n `12`; crypto_alt avg `-1.6878` n `233`; crypto_major avg `-0.7845` n `8`; equity avg `-0.2023` n `134`; fx avg `-0.0143` n `6`; index avg `0.0383` n `26`; metal avg `0.036` n `20`; unknown avg `-0.2411` n `709`
- 24h: commodity avg `-0.016` n `12`; crypto_alt avg `-3.4284` n `233`; crypto_major avg `-2.3026` n `8`; equity avg `-0.7098` n `134`; fx avg `0.0143` n `6`; index avg `-0.1455` n `26`; metal avg `0.5472` n `20`; unknown avg `1.8595` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
