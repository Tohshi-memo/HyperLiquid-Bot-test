# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T09:22:27.983577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0503` n `12`; crypto_alt avg `-0.0968` n `229`; crypto_major avg `-0.166` n `8`; equity avg `-0.0714` n `88`; fx avg `-0.0041` n `6`; index avg `-0.0026` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.0159` n `765`
- 1h: commodity avg `0.125` n `12`; crypto_alt avg `-0.2557` n `229`; crypto_major avg `-0.389` n `8`; equity avg `-0.0124` n `88`; fx avg `0.0063` n `6`; index avg `-0.0109` n `25`; metal avg `-0.0662` n `20`; unknown avg `-0.0646` n `765`
- 4h: commodity avg `0.0566` n `12`; crypto_alt avg `-0.3893` n `229`; crypto_major avg `-0.5567` n `8`; equity avg `0.0816` n `88`; fx avg `0.0283` n `6`; index avg `0.0562` n `25`; metal avg `0.1391` n `20`; unknown avg `-0.1661` n `731`
- 24h: commodity avg `-0.1488` n `12`; crypto_alt avg `-0.5382` n `229`; crypto_major avg `0.4422` n `8`; equity avg `-0.6057` n `88`; fx avg `0.0837` n `6`; index avg `-0.0182` n `25`; metal avg `-0.1856` n `20`; unknown avg `1.0129` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
