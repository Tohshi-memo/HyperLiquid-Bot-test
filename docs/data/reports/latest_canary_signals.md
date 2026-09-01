# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T21:22:26.361005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0335` n `12`; crypto_alt avg `-0.0468` n `232`; crypto_major avg `-0.0671` n `8`; equity avg `-0.0871` n `131`; fx avg `0.016` n `6`; index avg `-0.0086` n `26`; metal avg `0.0057` n `20`; unknown avg `-0.1001` n `787`
- 1h: commodity avg `-0.0487` n `12`; crypto_alt avg `-0.2689` n `232`; crypto_major avg `-0.2936` n `8`; equity avg `-0.1411` n `131`; fx avg `0.0105` n `6`; index avg `0.0045` n `26`; metal avg `0.0333` n `20`; unknown avg `0.0374` n `773`
- 4h: commodity avg `0.2473` n `12`; crypto_alt avg `-0.5099` n `232`; crypto_major avg `-0.8209` n `8`; equity avg `-0.1443` n `131`; fx avg `0.0148` n `6`; index avg `-0.0215` n `26`; metal avg `-0.1734` n `20`; unknown avg `1.739` n `773`
- 24h: commodity avg `0.8099` n `12`; crypto_alt avg `-0.3387` n `232`; crypto_major avg `-2.0882` n `8`; equity avg `-1.9516` n `130`; fx avg `0.0525` n `6`; index avg `-0.3433` n `26`; metal avg `-0.8554` n `20`; unknown avg `-0.3744` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0473`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0443`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0376`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0321`, n `668`, weak_sample_signal
