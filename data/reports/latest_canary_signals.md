# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T02:52:27.815073+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3117` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0413` n `12`; crypto_alt avg `-0.9394` n `234`; crypto_major avg `-0.6948` n `8`; equity avg `-0.2343` n `140`; fx avg `0.001` n `6`; index avg `-0.0244` n `26`; metal avg `-0.0043` n `20`; unknown avg `4.776` n `943`
- 1h: commodity avg `0.1102` n `12`; crypto_alt avg `-1.2999` n `234`; crypto_major avg `-0.9744` n `8`; equity avg `-0.2819` n `140`; fx avg `0.0065` n `6`; index avg `-0.0308` n `26`; metal avg `-0.0241` n `20`; unknown avg `6.5836` n `941`
- 4h: commodity avg `0.2986` n `12`; crypto_alt avg `-1.1821` n `234`; crypto_major avg `-1.355` n `8`; equity avg `-0.2183` n `140`; fx avg `-0.0041` n `6`; index avg `-0.0433` n `26`; metal avg `-0.0108` n `20`; unknown avg `2.3405` n `919`
- 24h: commodity avg `0.2068` n `12`; crypto_alt avg `-1.0082` n `234`; crypto_major avg `-2.085` n `8`; equity avg `-0.1522` n `140`; fx avg `-0.0558` n `6`; index avg `-0.0165` n `26`; metal avg `0.0091` n `20`; unknown avg `5.6976` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1675`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
