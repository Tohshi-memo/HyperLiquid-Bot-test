# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T04:07:31.801694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3357` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0655` n `12`; crypto_alt avg `-0.346` n `234`; crypto_major avg `-0.1777` n `8`; equity avg `-0.0566` n `141`; fx avg `-0.0051` n `6`; index avg `-0.0157` n `26`; metal avg `-0.0068` n `20`; unknown avg `1.336` n `952`
- 1h: commodity avg `0.1555` n `12`; crypto_alt avg `-0.8698` n `234`; crypto_major avg `-0.4543` n `8`; equity avg `-0.1794` n `141`; fx avg `-0.0145` n `6`; index avg `-0.0228` n `26`; metal avg `-0.0251` n `20`; unknown avg `1.5119` n `948`
- 4h: commodity avg `0.1204` n `12`; crypto_alt avg `-2.5415` n `234`; crypto_major avg `-1.536` n `8`; equity avg `-1.5184` n `141`; fx avg `0.0259` n `6`; index avg `-0.2003` n `26`; metal avg `-0.4921` n `20`; unknown avg `129.2082` n `936`
- 24h: commodity avg `-0.3172` n `12`; crypto_alt avg `-1.3522` n `234`; crypto_major avg `-1.5138` n `8`; equity avg `-1.5111` n `141`; fx avg `0.0465` n `6`; index avg `-0.1648` n `26`; metal avg `-0.6991` n `20`; unknown avg `14.0582` n `811`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
