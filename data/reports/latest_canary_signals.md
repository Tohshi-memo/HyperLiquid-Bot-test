# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T13:37:35.609702+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0601` n `13`; crypto_alt avg `-0.041` n `235`; crypto_major avg `0.2143` n `8`; equity avg `0.1274` n `150`; fx avg `-0.0061` n `6`; index avg `-0.0295` n `26`; metal avg `-0.0085` n `20`; unknown avg `35.8888` n `1074`
- 1h: commodity avg `0.1393` n `13`; crypto_alt avg `0.0105` n `235`; crypto_major avg `0.1522` n `8`; equity avg `0.1679` n `150`; fx avg `-0.045` n `6`; index avg `-0.0257` n `26`; metal avg `-0.0198` n `20`; unknown avg `22.1061` n `1072`
- 4h: commodity avg `0.0193` n `13`; crypto_alt avg `0.5132` n `235`; crypto_major avg `0.5513` n `8`; equity avg `0.3689` n `150`; fx avg `0.0326` n `6`; index avg `0.0402` n `26`; metal avg `-0.0459` n `20`; unknown avg `2.439` n `1064`
- 24h: commodity avg `-0.3874` n `13`; crypto_alt avg `-0.238` n `235`; crypto_major avg `0.1316` n `8`; equity avg `1.0018` n `149`; fx avg `0.094` n `6`; index avg `0.1939` n `26`; metal avg `-0.065` n `20`; unknown avg `1.3933` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1713`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
