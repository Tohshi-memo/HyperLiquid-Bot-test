# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T12:22:25.846521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0389` n `12`; crypto_alt avg `-0.0148` n `232`; crypto_major avg `0.0845` n `8`; equity avg `0.0319` n `134`; fx avg `-0.0202` n `6`; index avg `-0.0047` n `26`; metal avg `-0.1224` n `20`; unknown avg `0.8998` n `797`
- 1h: commodity avg `0.0102` n `12`; crypto_alt avg `-0.4363` n `232`; crypto_major avg `-0.3422` n `8`; equity avg `0.025` n `134`; fx avg `-0.0048` n `6`; index avg `-0.0163` n `26`; metal avg `-0.1067` n `20`; unknown avg `0.5328` n `795`
- 4h: commodity avg `-0.0408` n `12`; crypto_alt avg `0.0905` n `232`; crypto_major avg `-0.1397` n `8`; equity avg `0.6407` n `134`; fx avg `0.0098` n `6`; index avg `0.0838` n `26`; metal avg `-0.0255` n `20`; unknown avg `0.996` n `787`
- 24h: commodity avg `0.2878` n `12`; crypto_alt avg `-0.6217` n `232`; crypto_major avg `-1.5366` n `8`; equity avg `-0.0002` n `134`; fx avg `-0.1344` n `6`; index avg `-0.0336` n `26`; metal avg `0.0641` n `20`; unknown avg `-0.2817` n `710`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
