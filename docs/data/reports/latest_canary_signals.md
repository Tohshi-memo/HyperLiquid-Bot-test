# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T22:28:28.042540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.0297` n `230`; crypto_major avg `-0.1194` n `8`; equity avg `0.0198` n `96`; fx avg `-0.0092` n `6`; index avg `-0.0078` n `25`; metal avg `0.0137` n `20`; unknown avg `0.0837` n `769`
- 1h: commodity avg `0.003` n `12`; crypto_alt avg `-0.257` n `230`; crypto_major avg `-0.329` n `8`; equity avg `-0.0346` n `96`; fx avg `-0.007` n `6`; index avg `-0.0132` n `25`; metal avg `0.0227` n `20`; unknown avg `0.2227` n `769`
- 4h: commodity avg `0.0475` n `12`; crypto_alt avg `-0.3348` n `230`; crypto_major avg `-0.0071` n `8`; equity avg `-0.6489` n `96`; fx avg `-0.0601` n `6`; index avg `-0.1129` n `25`; metal avg `0.007` n `20`; unknown avg `-0.1737` n `769`
- 24h: commodity avg `0.6789` n `12`; crypto_alt avg `-1.3902` n `230`; crypto_major avg `-1.3011` n `8`; equity avg `-1.3595` n `94`; fx avg `0.0492` n `6`; index avg `-0.2987` n `25`; metal avg `0.0232` n `20`; unknown avg `-0.0294` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
