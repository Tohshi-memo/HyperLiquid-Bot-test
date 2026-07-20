# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T09:07:26.075952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0422` n `12`; crypto_alt avg `0.014` n `230`; crypto_major avg `-0.0888` n `8`; equity avg `-0.0234` n `98`; fx avg `-0.0202` n `6`; index avg `0.0169` n `25`; metal avg `-0.0295` n `20`; unknown avg `0.006` n `770`
- 1h: commodity avg `-0.0555` n `12`; crypto_alt avg `-0.1472` n `230`; crypto_major avg `-0.1762` n `8`; equity avg `-0.0945` n `98`; fx avg `-0.0247` n `6`; index avg `0.0155` n `25`; metal avg `-0.0756` n `20`; unknown avg `-0.0448` n `769`
- 4h: commodity avg `-0.4228` n `12`; crypto_alt avg `0.2525` n `230`; crypto_major avg `-0.279` n `8`; equity avg `-0.0995` n `98`; fx avg `-0.0057` n `6`; index avg `0.0209` n `25`; metal avg `0.0446` n `20`; unknown avg `-0.094` n `747`
- 24h: commodity avg `-0.5635` n `12`; crypto_alt avg `-0.2758` n `230`; crypto_major avg `-0.8291` n `8`; equity avg `-0.0565` n `97`; fx avg `-0.0284` n `6`; index avg `0.0288` n `25`; metal avg `0.1564` n `20`; unknown avg `-0.0615` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.103`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.097`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0895`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0804`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0773`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
