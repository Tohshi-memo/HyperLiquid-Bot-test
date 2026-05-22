# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T23:18:42.467712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0638` n `12`; crypto_alt avg `-0.2568` n `228`; crypto_major avg `-0.2231` n `8`; equity avg `-0.057` n `67`; fx avg `0.0` n `6`; index avg `-0.0097` n `23`; metal avg `-0.0054` n `18`; unknown avg `0.1251` n `386`
- 1h: commodity avg `0.1297` n `12`; crypto_alt avg `-0.2899` n `228`; crypto_major avg `-0.1765` n `8`; equity avg `-0.1424` n `67`; fx avg `0.0043` n `6`; index avg `-0.0376` n `23`; metal avg `-0.0364` n `18`; unknown avg `-0.0673` n `386`
- 4h: commodity avg `0.5241` n `12`; crypto_alt avg `-0.784` n `228`; crypto_major avg `-0.5963` n `8`; equity avg `-0.4318` n `67`; fx avg `0.0015` n `6`; index avg `-0.2243` n `23`; metal avg `-0.042` n `18`; unknown avg `0.5722` n `386`
- 24h: commodity avg `-0.4538` n `12`; crypto_alt avg `-2.8558` n `228`; crypto_major avg `-2.2723` n `8`; equity avg `-1.4781` n `67`; fx avg `0.1798` n `6`; index avg `0.3033` n `23`; metal avg `-1.0146` n `18`; unknown avg `-1.5203` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.05`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
