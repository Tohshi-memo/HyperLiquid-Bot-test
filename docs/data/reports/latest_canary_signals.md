# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T10:22:27.891804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0751` n `12`; crypto_alt avg `-0.222` n `228`; crypto_major avg `-0.2681` n `8`; equity avg `-0.2117` n `74`; fx avg `0.0124` n `6`; index avg `-0.0928` n `23`; metal avg `-0.2416` n `18`; unknown avg `1.0392` n `643`
- 1h: commodity avg `0.0478` n `12`; crypto_alt avg `0.0962` n `228`; crypto_major avg `-0.0976` n `8`; equity avg `0.0406` n `74`; fx avg `0.0422` n `6`; index avg `0.0226` n `23`; metal avg `-0.1323` n `18`; unknown avg `0.9619` n `643`
- 4h: commodity avg `-1.0599` n `12`; crypto_alt avg `1.3494` n `228`; crypto_major avg `0.871` n `8`; equity avg `0.6212` n `74`; fx avg `0.0095` n `6`; index avg `0.2968` n `23`; metal avg `0.4039` n `18`; unknown avg `0.4185` n `531`
- 24h: commodity avg `-2.4404` n `12`; crypto_alt avg `2.1861` n `228`; crypto_major avg `2.0484` n `8`; equity avg `2.7132` n `74`; fx avg `0.0419` n `6`; index avg `1.5677` n `23`; metal avg `3.2524` n `18`; unknown avg `-0.5109` n `514`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
