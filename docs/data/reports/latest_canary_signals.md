# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T16:37:35.998352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2835` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0098` n `12`; crypto_alt avg `-0.1688` n `234`; crypto_major avg `-0.2164` n `8`; equity avg `-0.0113` n `141`; fx avg `-0.0005` n `6`; index avg `-0.0016` n `26`; metal avg `0.0035` n `20`; unknown avg `0.3036` n `962`
- 1h: commodity avg `-0.0624` n `12`; crypto_alt avg `0.6027` n `234`; crypto_major avg `0.0766` n `8`; equity avg `0.042` n `141`; fx avg `0.0103` n `6`; index avg `0.0137` n `26`; metal avg `0.006` n `20`; unknown avg `0.0277` n `954`
- 4h: commodity avg `-0.1769` n `12`; crypto_alt avg `-1.0043` n `234`; crypto_major avg `-1.2788` n `8`; equity avg `-0.0713` n `141`; fx avg `0.0118` n `6`; index avg `0.0047` n `26`; metal avg `0.0011` n `20`; unknown avg `5.2873` n `954`
- 24h: commodity avg `-0.1202` n `12`; crypto_alt avg `-1.302` n `234`; crypto_major avg `-0.5613` n `8`; equity avg `0.1845` n `141`; fx avg `-0.013` n `6`; index avg `0.0141` n `26`; metal avg `-0.0093` n `20`; unknown avg `27.8848` n `897`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
