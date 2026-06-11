# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T08:22:32.556049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2093` n `12`; crypto_alt avg `0.3291` n `228`; crypto_major avg `0.2483` n `8`; equity avg `0.1103` n `74`; fx avg `-0.0075` n `6`; index avg `0.0168` n `23`; metal avg `-0.1813` n `18`; unknown avg `0.1191` n `556`
- 1h: commodity avg `-0.4498` n `12`; crypto_alt avg `0.2765` n `228`; crypto_major avg `0.2512` n `8`; equity avg `0.3781` n `74`; fx avg `-0.0407` n `6`; index avg `0.1451` n `23`; metal avg `-0.045` n `18`; unknown avg `0.1867` n `556`
- 4h: commodity avg `-1.1087` n `12`; crypto_alt avg `0.5532` n `228`; crypto_major avg `0.6247` n `8`; equity avg `0.9074` n `74`; fx avg `0.0218` n `6`; index avg `0.3766` n `23`; metal avg `0.4855` n `18`; unknown avg `0.1532` n `530`
- 24h: commodity avg `0.1364` n `12`; crypto_alt avg `1.3268` n `228`; crypto_major avg `1.3561` n `8`; equity avg `0.6924` n `74`; fx avg `0.0148` n `6`; index avg `-0.0181` n `23`; metal avg `-0.0434` n `18`; unknown avg `3.672` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
