# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T02:37:32.897695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0287` n `12`; crypto_alt avg `0.3799` n `231`; crypto_major avg `0.2241` n `8`; equity avg `0.1423` n `122`; fx avg `0.042` n `6`; index avg `0.0387` n `25`; metal avg `0.0111` n `20`; unknown avg `0.144` n `797`
- 1h: commodity avg `0.0332` n `12`; crypto_alt avg `0.6274` n `231`; crypto_major avg `0.2645` n `8`; equity avg `0.4212` n `122`; fx avg `-0.0065` n `6`; index avg `0.1069` n `25`; metal avg `0.1675` n `20`; unknown avg `0.1576` n `796`
- 4h: commodity avg `-0.0402` n `12`; crypto_alt avg `1.003` n `231`; crypto_major avg `0.4642` n `8`; equity avg `-0.2123` n `122`; fx avg `-0.0047` n `6`; index avg `-0.0255` n `25`; metal avg `0.0836` n `20`; unknown avg `0.2623` n `795`
- 24h: commodity avg `-0.8961` n `12`; crypto_alt avg `-2.443` n `231`; crypto_major avg `-2.6768` n `8`; equity avg `1.4985` n `122`; fx avg `0.0273` n `6`; index avg `0.2085` n `25`; metal avg `0.2542` n `20`; unknown avg `-0.3073` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
