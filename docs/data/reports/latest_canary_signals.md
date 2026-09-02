# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T18:37:27.798783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0719` n `12`; crypto_alt avg `0.014` n `232`; crypto_major avg `-0.1203` n `8`; equity avg `-0.0208` n `133`; fx avg `-0.0042` n `6`; index avg `-0.013` n `26`; metal avg `0.0143` n `20`; unknown avg `-0.001` n `792`
- 1h: commodity avg `-0.0422` n `12`; crypto_alt avg `0.2202` n `232`; crypto_major avg `0.2613` n `8`; equity avg `0.4555` n `133`; fx avg `-0.0017` n `6`; index avg `0.0294` n `26`; metal avg `0.07` n `20`; unknown avg `16.3036` n `790`
- 4h: commodity avg `0.1193` n `12`; crypto_alt avg `0.0991` n `232`; crypto_major avg `0.0181` n `8`; equity avg `0.3536` n `133`; fx avg `-0.0132` n `6`; index avg `0.0131` n `26`; metal avg `-0.0178` n `20`; unknown avg `15.317` n `789`
- 24h: commodity avg `0.1824` n `12`; crypto_alt avg `0.5366` n `232`; crypto_major avg `0.3733` n `8`; equity avg `0.8693` n `133`; fx avg `-0.3667` n `6`; index avg `0.1528` n `26`; metal avg `0.4222` n `20`; unknown avg `-0.0941` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0453`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
