# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T05:37:24.093790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `-0.0621` n `230`; crypto_major avg `0.0022` n `8`; equity avg `-0.0655` n `121`; fx avg `0.0308` n `6`; index avg `-0.0071` n `25`; metal avg `-0.0543` n `20`; unknown avg `-0.2549` n `792`
- 1h: commodity avg `-0.0097` n `12`; crypto_alt avg `0.2254` n `230`; crypto_major avg `0.4329` n `8`; equity avg `-0.071` n `121`; fx avg `0.0212` n `6`; index avg `-0.0182` n `25`; metal avg `-0.0654` n `20`; unknown avg `-0.2811` n `792`
- 4h: commodity avg `-0.0181` n `12`; crypto_alt avg `-0.0317` n `230`; crypto_major avg `0.1925` n `8`; equity avg `-0.0066` n `121`; fx avg `0.0422` n `6`; index avg `0.0109` n `25`; metal avg `-0.0588` n `20`; unknown avg `-0.1838` n `792`
- 24h: commodity avg `-0.0657` n `12`; crypto_alt avg `5.4518` n `230`; crypto_major avg `9.9329` n `8`; equity avg `1.3913` n `120`; fx avg `0.1421` n `6`; index avg `0.341` n `25`; metal avg `1.0389` n `20`; unknown avg `1.5625` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1957`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
