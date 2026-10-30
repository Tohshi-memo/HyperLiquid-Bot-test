# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T19:52:31.891178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0189` n `13`; crypto_alt avg `0.4124` n `238`; crypto_major avg `0.304` n `8`; equity avg `0.5532` n `156`; fx avg `-0.0063` n `6`; index avg `0.0574` n `27`; metal avg `0.0816` n `20`; unknown avg `0.3926` n `1259`
- 1h: commodity avg `-0.1898` n `13`; crypto_alt avg `1.1647` n `238`; crypto_major avg `0.9748` n `8`; equity avg `1.4892` n `156`; fx avg `0.0129` n `6`; index avg `0.1698` n `27`; metal avg `0.1475` n `20`; unknown avg `13.6776` n `1255`
- 4h: commodity avg `-0.1496` n `13`; crypto_alt avg `0.2185` n `238`; crypto_major avg `-0.2921` n `8`; equity avg `-0.1973` n `156`; fx avg `0.0408` n `6`; index avg `-0.039` n `27`; metal avg `-0.0355` n `20`; unknown avg `7.5628` n `1251`
- 24h: commodity avg `0.1527` n `13`; crypto_alt avg `-4.0417` n `238`; crypto_major avg `-3.9252` n `8`; equity avg `-5.4441` n `156`; fx avg `-0.0727` n `6`; index avg `-0.5087` n `27`; metal avg `-0.9921` n `20`; unknown avg `38.8839` n `1038`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.171`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1701`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
