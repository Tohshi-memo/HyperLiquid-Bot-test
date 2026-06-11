# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T05:37:26.293783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.089` n `12`; crypto_alt avg `-0.225` n `228`; crypto_major avg `-0.0202` n `8`; equity avg `-0.0382` n `74`; fx avg `0.0041` n `6`; index avg `0.0076` n `23`; metal avg `0.3587` n `18`; unknown avg `-0.0012` n `550`
- 1h: commodity avg `-0.4402` n `12`; crypto_alt avg `0.1584` n `228`; crypto_major avg `0.1596` n `8`; equity avg `0.0345` n `74`; fx avg `0.0149` n `6`; index avg `-0.015` n `23`; metal avg `0.419` n `18`; unknown avg `-0.1061` n `550`
- 4h: commodity avg `-0.2559` n `12`; crypto_alt avg `1.3038` n `228`; crypto_major avg `0.9611` n `8`; equity avg `0.0436` n `74`; fx avg `-0.0174` n `6`; index avg `0.117` n `23`; metal avg `-0.253` n `18`; unknown avg `3.9438` n `550`
- 24h: commodity avg `1.5612` n `12`; crypto_alt avg `1.6012` n `228`; crypto_major avg `1.1136` n `8`; equity avg `0.0072` n `74`; fx avg `0.0208` n `6`; index avg `-0.3914` n `23`; metal avg `-0.1637` n `18`; unknown avg `2.7987` n `537`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
