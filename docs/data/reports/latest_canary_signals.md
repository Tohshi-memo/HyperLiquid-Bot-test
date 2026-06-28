# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T17:37:28.841275+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.3048` n `228`; crypto_major avg `-0.3152` n `8`; equity avg `-0.0727` n `88`; fx avg `0.0` n `6`; index avg `0.0015` n `23`; metal avg `-0.0063` n `20`; unknown avg `0.6066` n `764`
- 1h: commodity avg `-0.0166` n `12`; crypto_alt avg `-0.3652` n `228`; crypto_major avg `-0.3155` n `8`; equity avg `-0.0514` n `88`; fx avg `-0.0227` n `6`; index avg `-0.0096` n `23`; metal avg `-0.0001` n `20`; unknown avg `0.6853` n `764`
- 4h: commodity avg `0.0625` n `12`; crypto_alt avg `-0.7229` n `228`; crypto_major avg `-0.9542` n `8`; equity avg `-0.1114` n `88`; fx avg `-0.0215` n `6`; index avg `-0.0207` n `23`; metal avg `-0.0368` n `20`; unknown avg `0.4711` n `764`
- 24h: commodity avg `0.3361` n `12`; crypto_alt avg `-1.2525` n `228`; crypto_major avg `-1.9456` n `8`; equity avg `0.0243` n `88`; fx avg `-0.025` n `6`; index avg `-0.0422` n `23`; metal avg `-0.0452` n `20`; unknown avg `14.8169` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1862`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
