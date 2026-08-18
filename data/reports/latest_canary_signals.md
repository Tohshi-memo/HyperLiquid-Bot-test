# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T10:22:26.722858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0625` n `12`; crypto_alt avg `-0.0063` n `230`; crypto_major avg `-0.006` n `8`; equity avg `-0.0748` n `114`; fx avg `-0.0117` n `6`; index avg `-0.0164` n `25`; metal avg `-0.012` n `20`; unknown avg `0.0325` n `795`
- 1h: commodity avg `0.0226` n `12`; crypto_alt avg `0.0219` n `230`; crypto_major avg `0.0024` n `8`; equity avg `-0.1631` n `114`; fx avg `-0.0225` n `6`; index avg `-0.0054` n `25`; metal avg `0.0466` n `20`; unknown avg `-0.013` n `795`
- 4h: commodity avg `-0.0893` n `12`; crypto_alt avg `0.0562` n `230`; crypto_major avg `-0.2462` n `8`; equity avg `-1.1632` n `114`; fx avg `-0.0395` n `6`; index avg `-0.1304` n `25`; metal avg `-0.1498` n `20`; unknown avg `0.0606` n `793`
- 24h: commodity avg `0.5098` n `12`; crypto_alt avg `-0.5422` n `230`; crypto_major avg `0.2249` n `8`; equity avg `-2.8107` n `114`; fx avg `-0.056` n `6`; index avg `-0.5513` n `25`; metal avg `-0.2372` n `20`; unknown avg `0.0333` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
