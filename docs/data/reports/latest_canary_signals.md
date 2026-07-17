# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T22:22:25.312348+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.054` n `12`; crypto_alt avg `-0.0135` n `230`; crypto_major avg `-0.0406` n `8`; equity avg `0.0627` n `96`; fx avg `-0.0092` n `6`; index avg `-0.0095` n `25`; metal avg `0.01` n `20`; unknown avg `0.0284` n `769`
- 1h: commodity avg `-0.0457` n `12`; crypto_alt avg `-0.2409` n `230`; crypto_major avg `-0.2502` n `8`; equity avg `0.0084` n `96`; fx avg `-0.007` n `6`; index avg `-0.0148` n `25`; metal avg `0.019` n `20`; unknown avg `0.1626` n `769`
- 4h: commodity avg `-0.0012` n `12`; crypto_alt avg `-0.3183` n `230`; crypto_major avg `0.0719` n `8`; equity avg `-0.6071` n `96`; fx avg `-0.0601` n `6`; index avg `-0.1146` n `25`; metal avg `0.0033` n `20`; unknown avg `-0.1913` n `769`
- 24h: commodity avg `0.6286` n `12`; crypto_alt avg `-1.3736` n `230`; crypto_major avg `-1.2244` n `8`; equity avg `-1.3186` n `94`; fx avg `0.0492` n `6`; index avg `-0.3004` n `25`; metal avg `0.0195` n `20`; unknown avg `-0.0264` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
