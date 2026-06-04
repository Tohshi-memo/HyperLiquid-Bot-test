# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T01:37:22.550533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.0045` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.6047` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.5855` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1504` n `12`; crypto_alt avg `0.2375` n `228`; crypto_major avg `0.2532` n `8`; equity avg `0.0908` n `73`; fx avg `0.0032` n `6`; index avg `0.0592` n `23`; metal avg `-0.1054` n `18`; unknown avg `-0.1732` n `420`
- 1h: commodity avg `-0.3327` n `12`; crypto_alt avg `-1.3375` n `228`; crypto_major avg `-0.8085` n `8`; equity avg `-0.2078` n `73`; fx avg `0.0065` n `6`; index avg `0.0388` n `23`; metal avg `0.41` n `18`; unknown avg `-0.323` n `419`
- 4h: commodity avg `-0.7782` n `12`; crypto_alt avg `-2.9152` n `228`; crypto_major avg `-2.4796` n `8`; equity avg `0.1059` n `73`; fx avg `-0.0065` n `6`; index avg `0.1251` n `23`; metal avg `0.5249` n `18`; unknown avg `-0.3877` n `419`
- 24h: commodity avg `-0.0887` n `12`; crypto_alt avg `-1.0713` n `228`; crypto_major avg `-2.7492` n `8`; equity avg `-3.4047` n `72`; fx avg `0.0319` n `6`; index avg `-0.9902` n `23`; metal avg `-1.2356` n `18`; unknown avg `0.5372` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
