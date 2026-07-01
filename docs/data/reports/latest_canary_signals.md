# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T08:37:29.789506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.281` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.103` n `12`; crypto_alt avg `0.0137` n `228`; crypto_major avg `-0.0447` n `8`; equity avg `-0.0776` n `88`; fx avg `0.0015` n `6`; index avg `0.0051` n `23`; metal avg `-0.0638` n `20`; unknown avg `-0.0818` n `765`
- 1h: commodity avg `-0.233` n `12`; crypto_alt avg `-0.138` n `228`; crypto_major avg `-0.4024` n `8`; equity avg `-0.0254` n `88`; fx avg `-0.0015` n `6`; index avg `0.0078` n `23`; metal avg `0.0473` n `20`; unknown avg `0.1898` n `765`
- 4h: commodity avg `-0.3022` n `12`; crypto_alt avg `-1.0395` n `228`; crypto_major avg `-1.3364` n `8`; equity avg `-0.3802` n `88`; fx avg `-0.0167` n `6`; index avg `-0.0554` n `23`; metal avg `-0.0494` n `20`; unknown avg `-0.0669` n `743`
- 24h: commodity avg `-0.4169` n `12`; crypto_alt avg `-0.5649` n `228`; crypto_major avg `-0.7248` n `8`; equity avg `0.4177` n `88`; fx avg `0.0802` n `6`; index avg `0.001` n `23`; metal avg `-0.6791` n `20`; unknown avg `-0.1981` n `743`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
